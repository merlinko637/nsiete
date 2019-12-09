const path = require('path');
const fs = require('fs');
const math = require('mathjs');
const sizeOf = require('image-size');
const directoryPath = 'C:\\Users\\Predu\\Skola\\NSIETE\\Projekt\\nsiete\\data\\dataset';
var EXTENSIONTXT = '.txt';
var leftX = [], topY = [], widthECV = [], heightECV = [], heightImg = [], widthImg = [];

fs.readdir(directoryPath, function (err, files) {

    if (err) {
        return console.log('Unable to scan directory: ' + err);
    }

    var targetFiles = files.filter(function(file) {
      return path.extname(file).toLowerCase() === EXTENSIONTXT;
    });

    var targetImgs = files.filter(function(file) {
      return path.extname(file).toLowerCase() !== EXTENSIONTXT;
    });

    targetFiles.forEach(function (file) {

        fs.readFile(path.join(directoryPath, file), (err, data) => {

          if (err) {
            return console.log('Unable to open file: ' + err);
          }

          var splitted = data.toString().match(/\S+/g);
          leftX.push(parseInt(splitted[1]));
          topY.push(parseInt(splitted[2]));
          widthECV.push(parseInt(splitted[3]));
          heightECV.push(parseInt(splitted[4]));

        });
    });

    targetImgs.forEach(function (file) {

        var dimensions = sizeOf(path.join(directoryPath, file));
        heightImg.push(dimensions.height);
        widthImg.push(dimensions.width);

    });

    setTimeout(function(){
      console.log("Priemerna sirka a vyska obrazku: [" + math.mean(widthImg).toFixed(2) + ", "+ math.mean(heightImg).toFixed(2) +"]");
      console.log("Standardna odchylka sirky a vysky obrazku: [" + math.std(widthImg).toFixed(2) + ", "+ math.std(heightImg).toFixed(2) +"]");
      console.log("Priemerna poloha laveho horneho rohu ECV: [" + math.mean(leftX).toFixed(2) + ", "+ math.mean(topY).toFixed(2) +"]");
      console.log("Standardna odchylka polohy laveho horneho rohu ECV: [" + math.std(leftX).toFixed(2) + ", "+ math.std(topY).toFixed(2) +"]");
      console.log("Priemerna sirka a vyska ECV: [" + math.mean(widthECV).toFixed(2) + ", "+ math.mean(heightECV).toFixed(2) +"]");
      console.log("Standardna odchylka sirky a vysky ECV: [" + math.std(widthECV).toFixed(2) + ", "+ math.std(heightECV).toFixed(2) +"]");
    }, 1000);
});
