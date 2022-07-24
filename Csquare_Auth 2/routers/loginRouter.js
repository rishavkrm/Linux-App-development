const express = require('express')
const app = express();
const User = require('../model/userModel')
const demoUser = require('../model/demoUserModel')
const AppError = require('./../errorHandler/AppError')
const bcrypt = require('bcrypt')
const checkOtpExpiry = function(otpExpiryTime){
    return Date.now() < otpExpiryTime;
}

const loginRouter = express.Router()
const login = async (req,res,next)=>{
    try{

        const email = req.body.email;
        const password = req.body.password;
        console.log(email,password)
        if (!email || !password) {
            return(next(new AppError('Email or Password not provided'),403));
        }
             
        const user = await User.findOne({email:email})
        console.log(user)
        if(!user){
            console.log('No user found by this email id')
            return(next(new AppError('No user found by this email id'),403))
        }
        
        const result = await bcrypt.compare(password,user.password);
        console.log(result)
        if(! result){
            console.log('User password does not match.')
            return(next(new AppError(`Password doesn't match`, 400)))
        }
        console.log("HI")
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



loginRouter.route('/')
.post(login)


module.exports = loginRouter