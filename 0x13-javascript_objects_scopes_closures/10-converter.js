#!/usr/bin/node

exports.converter = function (base) {
  return function (ads) {
    return ads.toString(base);
  };
};
