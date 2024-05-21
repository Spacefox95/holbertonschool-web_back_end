function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  const result = [];
  for (const value of set) {
    if (typeof startString === 'string' && value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  }
  return result.join('-');
}
export default cleanSet;
