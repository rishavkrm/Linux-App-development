const mongoose = require('mongoose')
userDemoSchema = mongoose.Schema({
    email:{
        type:String,
        required:[true,"Email is required!"],
        trim:true
    },
    otp:{
        type:String
    },
    otpExpiryTime:{
        type:Date
    },
    otpCreatedAt:{
        type:Date
    }
})

const demoUser = new mongoose.model('demoUser',userDemoSchema);


module.exports = demoUser