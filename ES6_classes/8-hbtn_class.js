export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size === 'number') {
      this._size = size;
    }
    if (typeof location === 'string') {
      this._location = location;
    }
  }

  [Symbol.toPrimitive](type) {
    if (type === 'string') return this._location;
    return this._size;
  }
}
