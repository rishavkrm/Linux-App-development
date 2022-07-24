const express = require('express')
const app = express();
const User = require('./../model/userModel')
const AppError = require('./../errorHandler/AppError')
const demoUser = require('./../model/demoUserModel')
const Email = require('./../email');

const checkOtpExpiry = function(otpExpiryTime){
    return Date.now() < otpExpiryTime;
}

const registerRouter = express.Router()

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
const sendMailForReset = async (req,res,next)=>{
    try {
        async function generateRandomIntegerInRange(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        const otpCreatedAt = Date.now()
        const otpExpiryTime = otpCreatedAt + 5 * 60 * 1000;
        const user = await demoUser.findOneAndUpdate({email:req.body.email},{otp:String(await generateRandomIntegerInRange(1000,9999)),otpExpiryTime:otpExpiryTime});
        console.log(Boolean(user))
        if(!user){
            return(next(new AppError('User not found'),404));
        }
        const message = "Hello there! Your otp for verification is "+user.otp
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

const checkOtpAndUpdateUser = async (req,res,next)=>{
    try{
        const sentOtp = req.body.otp
        const cookies = parseCookies(req);
        // console.log(cookies['email'])
        const email = cookies['email'];
        
        if (!email || !req.body.newPassword || !req.body.confirmNewPassword) {
            return(next(new AppError('Email or Password not provided'),403));
        }
        
        console.log(sentOtp)
        
        const user = await demoUser.findOne({email:email});
        console.log(user)
        if(!user){
            return(next(new AppError('Not found'),403))
        }
        const otp =  user.otp;
        if(!checkOtpExpiry(user.otpExpiryTime)){
            return(next(new AppError('Otp expired'),400))
        }
        if(String(otp) != String(sentOtp)){
            return(next(new AppError('Please enter correct otp'),403))
        }
        
        
        const password = req.body.newPassword;
        const passwordConfirm = req.body.confirmNewPassword;
        const userId = req.body.userId
        const name = req.body.name;
        const doc = await User.findOne({email:email});
        doc.password = req.body.newPassword;
        doc.passwordConfirm = req.body.confirmNewPassword;
        doc.userId = userId;
        doc.name = name;
        await doc.save();
        
        
        res.status(200).json({
            status:"success",
            message:'Created one new User',
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


registerRouter.route('/sendMail')
.post(sendMailForReset)
registerRouter.route('/otp')
.post(checkOtpAndUpdateUser)

module.exports = registerRouter