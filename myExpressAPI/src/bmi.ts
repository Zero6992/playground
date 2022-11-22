import express from "express";
import bmiCalculator from '@infinitetoolbox/bmi-calculator';

const app = express();

app.get('/bmi', (req, res) => {
    const weight = req.query.weight as unknown as number
    const height = req.query.height as unknown as number
    const bmi = bmiCalculator(weight, height / 100);

    if(!weight || !height){
        return res.status(415).json({
            message:"Unsupported Media Type"
        });
    }
    return  res.status(200).json({
        bmi: bmi
    })
})

app.listen(8000, () => {
    console.log("Server is up and running")
})