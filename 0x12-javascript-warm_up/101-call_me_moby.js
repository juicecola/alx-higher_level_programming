#!/usr/bin/node
exports.callMeMoby = function (x, thefunction) {
  let i = 0;
  for (i = 0; i < x; i++) {
    thefunction();
  }
};
