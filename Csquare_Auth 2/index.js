const http = require('http')
const dotenv = require('dotenv');
const express = require('express')
const app = express()
const mongoose = require('mongoose')

const globalErrorHandler = require('./errorHandler/errorHandler') 
const AppError = require('./errorHandler/AppError')
const createRouter = require('./routers/createRouter')
const resetRouter = require('./routers/resetRouter')
const loginRouter = require('./routers/loginRouter')

const registerRouter = require('./auth')


dotenv.config({ path: './config.env' });
const DB = process.env.DATABASE.replace('<PASSWORD>',process.env.DB_PASSWORD)
mongoose.connect(DB)
.then((con)=>console.log("Connection succesful"))

// -------------
app.use(express.json({limit:'100kb'}));
app.use('/create',createRouter)
app.use('/reset',resetRouter)
app.use('/login',loginRouter)

console.log(AppError)
app.all('*', (req, res, next) => {
    console.log(`Can't find ${req.originalUrl} on this server!`)
    next(new AppError(`Can't find ${req.originalUrl} on this server!`, 404));
  });
console.log('Using global error handler')
app.use(globalErrorHandler);
app.listen('3000',()=>{
    "App listening on port 3000."
})