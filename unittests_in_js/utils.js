const Utils = {
  calculateNumber(type, a, b) {
  const numA = Number(a);
  const numB = Number(b);

  if (Number.isNaN(numA) || Number.isNaN(numB))
  throw TypeError;

  if (type === 'SUM') {
    return (Math.round(numA) + Math.round(numB));
  } else if (type === 'SUBTRACT') {
    return (Math.round(numA) - Math.round(numB));
  } else if (type === 'DIVIDE') {
      if (Math.round(numB) === 0) {
        return ('Error');
      }
      return (Math.round(numA) / Math.round(numB));
  } else {
    throw TypeError;
  }
}
};

module.exports = Utils;