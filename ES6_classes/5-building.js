export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building) {
      if (!this.evacuationWarningMessage) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
    this._sqft = sqft;
  }

  // Getter
  get sqft() {
    return this._sqft;
  }
}
