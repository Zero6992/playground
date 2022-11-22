import "reflect-metadata"
import express from "express";

const app = express();

const authIDcard = (autoIDcard: string) => {
    let county = "";
    let authCode = 0;
    const MOD = 10;

    const firstLetter = autoIDcard.charAt(0)
    const checkCode = Number(autoIDcard.charAt(9))
    let firstLetterCode: number = 0;

    switch (firstLetter) {
        case "A":
            county = "台北市"
            firstLetterCode = 10;
            break;
        case "B":
            county = "台中市"
            firstLetterCode = 11;
            break;
        case "C":
            county = "基隆市"
            firstLetterCode = 12;
            break;
        case "D":
            county = "台南市"
            firstLetterCode = 13;
            break;
        case "E":
            county = "高雄市"
            firstLetterCode = 14;
            break;
        case "F":
            county = "新北市"
            firstLetterCode = 15;
            break;
        case "G":
            county = "宜蘭縣"
            firstLetterCode = 16;
            break;
        case "H":
            county = "桃園縣"
            firstLetterCode = 17;
            break;
        case "J":
            county = "新竹縣"
            firstLetterCode = 18;
            break;
        case "K":
            county = "苗栗縣"
            firstLetterCode = 19;
            break;
        case "L":
            county = "台中縣"
            firstLetterCode = 20;
            break;
        case "M":
            county = "南投縣"
            firstLetterCode = 21;
            break;
        case "N":
            county = "彰化縣"
            firstLetterCode = 22;
            break;
        case "O":
            county = "新竹市"
            firstLetterCode = 35;
            break;
        case "P":
            county = "雲林縣"
            firstLetterCode = 23;
            break;
        case "Q":
            county = "嘉義縣"
            firstLetterCode = 24;
            break;
        case "R":
            county = "台南縣"
            firstLetterCode = 25;
            break;
        case "S":
            county = "高雄縣"
            firstLetterCode = 26;
            break;
        case "T":
            county = "屏東縣"
            firstLetterCode = 27;
            break;
        case "U":
            county = "花蓮縣"
            firstLetterCode = 28;
        case "V":
            county = "台東縣"
            firstLetterCode = 29;
            break;
        case "W":
            county = "金門縣"
            firstLetterCode = 32;
            break;
        case "X":
            county = "澎湖縣"
            firstLetterCode = 30;
            break;
        case "Z":
            county = "連江縣"
            firstLetterCode = 33;
        case "Y":
            county = "陽明山"
            firstLetterCode = 31;
            break;
        default:
            break;
    }
    for (let index = 1, weight = 8; index <= 8; index++, weight--) {
        let temp = Number(autoIDcard.charAt(index))
        authCode += temp * weight
    }

    let firstLetterCodeChar = firstLetterCode.toString()
    authCode += Number(firstLetterCodeChar.charAt(0)) * 1
    authCode += Number(firstLetterCodeChar.charAt(1)) * 9

    let remainder = 0
    remainder = authCode % MOD;
    if (remainder) {
        authCode = MOD - remainder
    } else {
        authCode = 0;
    }

    if (checkCode == authCode) {
        return true
    }
    return false
}

const whichCounty = (autoIDcard: string) => {
    const firstLetter = autoIDcard.charAt(0)
    let county = "";
    switch (firstLetter) {
        case "A":
            county = "台北市"
            break;
        case "B":
            county = "台中市"
            break;
        case "C":
            county = "基隆市"
            break;
        case "D":
            county = "台南市"
            break;
        case "E":
            county = "高雄市"
            break;
        case "F":
            county = "新北市"
            break;
        case "G":
            county = "宜蘭縣"
            break;
        case "H":
            county = "桃園縣"
            break;
        case "J":
            county = "新竹縣"
            break;
        case "K":
            county = "苗栗縣"
            break;
        case "L":
            county = "台中縣"
            break;
        case "M":
            county = "南投縣"
            break;
        case "N":
            county = "彰化縣"
            break;
        case "O":
            county = "新竹市"
            break;
        case "P":
            county = "雲林縣"
            break;
        case "Q":
            county = "嘉義縣"
            break;
        case "R":
            county = "台南縣"
            break;
        case "S":
            county = "高雄縣"
            break;
        case "T":
            county = "屏東縣"
            break;
        case "U":
            county = "花蓮縣"
        case "V":
            county = "台東縣"
            break;
        case "W":
            county = "金門縣"
            break;
        case "X":
            county = "澎湖縣"
            break;
        case "Z":
            county = "連江縣"
            break;
        case "Y":
            county = "陽明山"
            break;
        default:
            county = "格式錯誤"
            break;
    }

    return county
}

const authGender = (autoIDcard: string) => {
    const genderCode = Number(autoIDcard.charAt(1))
    let gender = "格式錯誤";
    if (genderCode == 1) {
        gender = "男性";
    } else if (genderCode == 2) {
        gender = "女性";

    } else {
        gender = "格式錯誤";
    }

    return gender
}
app.get('/auth', (req, res) => {
    const IDcard = req.query.IDcard as unknown as string;
    const gender = authGender(IDcard);
    const authCode = authIDcard(IDcard);
    const county = whichCounty(IDcard);


    if (!IDcard) {
        return res.status(415).json({
            message: "Unsupported Media Type"
        });
    } else if (!authCode) {
        return res.status(666).json({
            valid: authCode
        });
    }
    return res.status(200).json({
        gender: gender,
        county: county,
        valid: authCode
    })
})

app.listen(9000, () => {
    console.log("Server is up and running")
})