#!/usr/bin/node

exports.esrever = function (zer) {
  const zerz = [];
  for (let j = zer.length - 1; j >= 0; j--) {
    zerz.push(zer[j]);
  }
  return zerz;
};
