const express = require('express')
const app = express();
const User = require('./model/userModel')
const {Error} = require('mongoose')
const bcrypt = require('bcrypt')

const registerRouter = express.Router()

const registerUser = async (req,res,next)=>{
    try{
        const email = req.body.email;
        console.log(email)
        const password = req.body.password;
        console.log(password)
        if (!email || !password) {
            next(new Error('Email or Password not provided'));
        }
        const doc = await User.create({email:email,password:password,passwordConfirm:req.body.passwordConfirm});
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

const resetPassword = async (req,res,next)=>{
    try{

        const email = req.body.email;
        const currentPassword = req.body.currentPassword;
        const newPassword = req.body.newPassword;
        const confirmNewPassword = req.body.confirmNewPassword
        
        if (!email || !currentPassword || !confirmNewPassword || !newPassword) {
            next(new Error('Email or Password not provided'));
        }
        console.log(email,currentPassword,newPassword,confirmNewPassword)

        

        if(newPassword != confirmNewPassword){
            console.log('Password and Confirm password are not same.')
            next(new Error('Password and Confirm password are not same.'))
        }        
        console.log(email,currentPassword,newPassword,confirmNewPassword)

        const user = await User.findOne({email:email})
        console.log(user)
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
const forgotPassword = async (req,res,next)=>{
    try{

        const email = req.body.email;
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

registerRouter.route('/register')
.post(registerUser)
registerRouter.route('/login')
.post(login)
registerRouter.route('/reset')
.post(resetPassword)
registerRouter.route('/forgot')
.post(forgotPassword)

module.exports = registerRouter