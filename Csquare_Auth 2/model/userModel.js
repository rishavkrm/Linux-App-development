const mongoose = require('mongoose')
const bcrypt = require('bcrypt')

userSchema = mongoose.Schema({

    name:{
        type:String,
        required:[true,"Name is required"]
    },
    userId:{
        type:String,
        required:[true,"UserId is required"],
        unique:[true,"UserId already exists"]
    },
    email:{
        type:String,
        required:[true,"Email is required!"],
        trim:true,
        unique:[true,"Email already exists"]
    },
    password:{
        type:String,
        required:[true,"Password is required."],
        minlength:8
        // ,select:false
    },
    passwordConfirm:{
        type:String,
        required:[true,"Plaese confirm your password"],
        minlength:8,
        validate:{
            //Only works on create and save!!!!!!!!!!!!!
            validator:function(el){
                return el===this.password;
            },
        message:"Passwords are not same"
        }}
},{validateBeforeSave:true})

userSchema.pre('save', async function(next){

    if(this.isNew)
    {   
        return next()
    }
    console.log('Hi')
    this.password = await bcrypt.hash(this.password, 12);//asyc
    this.passwordConfirm = undefined;
    next();
})


const User = new mongoose.model('User',userSchema);


module.exports = User