const express = require('express')
const app = express();
const User = require('./../model/userModel')
const demoUser = require('./../model/demoUserModel')
const AppError = require('./../errorHandler/AppError')
const Email = require('./../email');

const checkOtpExpiry = function(otpExpiryTime){
    return Date.now() < otpExpiryTime;
}


const createRouter = express.Router()

function parseCookies (request) {
    const list = {};
    const cookieHeader = request.headers?.cookie;
    if (!cookieHeader) return list;

    cookieHeader.split(`;`).forEach(function(cookie) {
        let [ name, ...rest] = cookie.split(`=`);
        name = name?.trim();
        if (!name) return;
        const value = rest.join(`=`).trim();
        if (!value) return;
        list[name] = decodeURIComponent(value);
    });

    return list;
}

const sendMailForCreate = async (req,res,next)=>{
    try {
        async function generateRandomIntegerInRange(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        const otpCreatedAt = Date.now()
        const otpExpiryTime = otpCreatedAt + 5 * 60 * 1000;
        let duplicateUser = await User.findOne({email:req.body.email});
        if(duplicateUser){
            return(next(new AppError('Email already exists'),400))
        }
        duplicateUser = await User.findOne({userId:req.body.userId});
        if(duplicateUser){
            return(next(new AppError('UserId already exists'),400))
        }
        const user = await demoUser.create({email:req.body.email,otp:String(await generateRandomIntegerInRange(1000,9999)),otpExpiryTime:otpExpiryTime,otpCreatedAt:otpCreatedAt});
        const message = "Hello there! Your otp for verification is "+user.otp;
        await Email({
            email: req.body.email,
            subject: 'Your password reset OTP',
            message
          });
        res.cookie(`email`,req.body.email);    
        res.status(200).json({
          status: 'success',
          message: 'Token sent to email!'
        });
      }
      catch(err){
        res.json({
            status:"error",
            err:err
        })
      }
}
const checkOtpAndMakeUser = async (req,res,next)=>{
    try{
        sentOtp = req.body.otp;
        if(!sentOtp){
            return(next(new AppError('Please enter otp.'),403))
        }
    
        const cookies = parseCookies(req);
        const id = cookies['email'];
        if (!id || !req.body.password || !req.body.passwordConfirm) {
            return(next(new AppError('Email or Password not provided'),403));
        };
        const user = await demoUser.findOne({email:id});
        if(!user){
            return(next(new AppError('Not found'),404))
        }
        const otp =  user.otp;
        console.log(otp)
        if(!checkOtpExpiry(user.otpExpiryTime)){
            return(next(new AppError('Otp expired'),400))
        }
        if(String(otp) != String(sentOtp)){
            return(next(new AppError('Please enter correct otp'),403))
        } 
        const email = id;
        const password = req.body.password;
        const passwordConfirm = req.body.passwordConfirm;
        const doc = await User.create({email:email,password:password,passwordConfirm:passwordConfirm});
        await User.findOneAndUpdate({email:doc.email},{passwordConfirm:undefined})
        res.status(200).json({
            status:"success",
            message:'Created new User',
            result:doc
        })

    }
    catch(err){
        res.status(404).json({
            status:'fail',
            err:err
        })
    }

}
createRouter.route('/sendMail')
.post(sendMailForCreate)
createRouter.route('/otp')
.post(checkOtpAndMakeUser)


module.exports = createRouter