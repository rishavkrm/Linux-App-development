const express = require('express')
const app = express();
const User = require('./model/userModel')
const demoUser = require('./model/demoUserModel')
const {Error} = require('mongoose')
const bcrypt = require('bcrypt')
const Email = require('./email');
const http = require('http');
const cookieParser = require('cookie-parser')

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

const sendMailForCreate = async (req,res,next)=>{
    try {
        async function generateRandomIntegerInRange(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        const user = await demoUser.create({email:req.body.email,otp:String(await generateRandomIntegerInRange(1000,9999))});
        const message = "Hello there! Your otp for verification is "+user[0].otp;
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
            new Error('Please enter otp.')
        }
        const cookies = parseCookies(req);
        const id = cookies['email'];
        if (!id || !req.body.password || !req.body.passwordConfirm) {
            next(new Error('Email or Password not provided'));
        };
        const user = await demoUser.findOne({email:id});
        if(!user){
            next(new Error('Not found'))
        }
        const otp =  user.otp;
        console.log(otp)
        if(String(otp) != String(sentOtp)){
            next(new Error('Please enter correct otp'))
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


const sendMailForReset = async (req,res,next)=>{
    try {
        async function generateRandomIntegerInRange(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        console.log('user')
        const user = await User.findOneAndUpdate({email:req.body.email},{otp:String(await generateRandomIntegerInRange(1000,9999))},{ validateBeforeSave: false });
        console.log(user)
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
        sentOtp = req.body.otp;
        console.log(sendOtp)
        const email = parseCookies(req)[email];
        if (!email || !req.body.newPassword || !req.body.confirmNewPassword) {
            next(new Error('Email or Password not provided'));
        }
       
        const user = await User.findOne({email:email});
        console.log(user)
        if(!user){
            next(new Error('Not found'))
        }
        console.log(user)
        const otp =  user.otp;
        console.log(otp);
        if(String(otp) != String(sentOtp)){
            next(new Error('Please enter correct otp'))
        }
        
        const password = req.body.newPassword;
        console.log(password)
        const passwordConfirm = req.body.confirmNewPassword;
        console.log(password)
        
        const doc = await User.findOneAndUpdate({email:email},{password:password,passwordConfirm:req.body.passwordConfirm});
        await User.findOneAndUpdate({email:doc.email},{otp:undefined},{passwordConfirm:undefined})
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

const forgotPassword = async (req,res,next)=>{
    try{

        const email = parseCookies(req)[email];
        if (!email) {
            next(new Error('Email not provided'));
        }

        const user = await User.findOne({email:email})
        if(!user){
            console.log('No user found by this email id')
            next(new Error('No user found by this email id'))
        }
        
        const result = await bcrypt.compare(currentPassword,user.password);
        console.log(result)
        if(! result){
            console.log('User password does not match.')
            next(new Error('User password does not match.'))
        }


        const Password = await bcrypt.hash(newPassword,12)
        console.log(Password)

        const doc = await User.findOneAndUpdate({email:email},{password:Password});
        console.log(doc)
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

const login = async (req,res,next)=>{
    try{

        const email = req.body.email;
        const password = req.body.password;
        console.log(email,password)
        if (!email || !password) {
            next(new Error('Email or Password not provided'));
        }
             
        const user = await User.findOne({email:email})
        console.log(user)
        if(!user){
            console.log('No user found by this email id')
            next(new Error('No user found by this email id'))
        }
        
        const result = await bcrypt.compare(password,user.password);
        console.log(result)
        if(! result){
            console.log('User password does not match.')
            next(new Error('User password does not match.'))
        }
        res.status(200).json({
            status:"success",
            message:'Found new User',
            result:user
        })
    }
    catch(err){
        res.status(404).json({
            status:'fail',
            err:err
        })
    }

}


registerRouter.route('/create/sendMail')
.post(sendMailForCreate)
registerRouter.route('/create/otp')
.post(checkOtpAndMakeUser)
registerRouter.route('/login')
.post(login)
registerRouter.route('/reset/sendMail')
.post(sendMailForReset)
registerRouter.route('/reset/otp')
.post(checkOtpAndUpdateUser)
registerRouter.route('/forgot/sendMail')
.post(sendMailForReset)
registerRouter.route('/forgot/otp')
.post(checkOtpAndUpdateUser)

module.exports = registerRouter