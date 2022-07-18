const http = require('http')
const dotenv = require('dotenv');
const express = require('express')
const app = express()
const mongoose = require('mongoose')

const registerRouter = require('./auth')

dotenv.config({ path: './config.env' });
const DB = process.env.DATABASE.replace('<PASSWORD>',process.env.DB_PASSWORD)
mongoose.connect(DB)
.then((con)=>console.log("Connection succesful"))

// -------------
app.use(express.json({limit:'100kb'}));
app.use('/',registerRouter)


app.listen('3000',()=>{
    "App listening on port 3000."
})