function updateUniqueItems(list) {
  if (!(list instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [key, value] of list) {
    if (value === 1) {
      list.set(key, 100);
    }
  }
  return list;
}
export default updateUniqueItems;
