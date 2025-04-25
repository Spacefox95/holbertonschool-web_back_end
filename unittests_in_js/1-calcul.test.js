const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", function () {
  it("Sum when both are integers.", () => {
    assert.strictEqual(calculateNumber(1, 3, 'SUM'), 4);
  });

  it("Sum when b is a float.", () => {
    assert.strictEqual(calculateNumber(1, 3.7, 'SUM'), 5);
  });

  it("Sum when a is rounded down & b is rounded up.", () => {
    assert.strictEqual(calculateNumber(1.2, 3.7, 'SUM'), 5);
  });

  it("Sum when a is a float.", () => {
    assert.strictEqual(calculateNumber(1.2, 3, 'SUM'), 4);
  });

  it("Subtract when a is rounded up & b is rounded down.", () => {
    assert.strictEqual(calculateNumber(1.7, 3.2, 'SUBTRACT'), -1);
  });

  it("Subtract when both are rounded up.", () => {
    assert.strictEqual(calculateNumber(1.5, 3.7, 'SUBTRACT'), -2);
  });
	it("Divide when both are rounded up.", () => {
    assert.strictEqual(calculateNumber(1.5, 3.7, 'DIVIDE'), 0.5);
  });
	it("Sum when both are rounded up.", () => {
    assert.strictEqual(calculateNumber(1.4, 4.5, 'SUBTRACT'), -4);
  });
	it("Sum when both are rounded up.", () => {
    assert.strictEqual(calculateNumber(1.4, 4.5, 'DIVIDE'), 0.2);
  });
	it("Sum when both are rounded up.", () => {
    assert.strictEqual(calculateNumber(1.4, 0, 'DIVIDE'), 'Error');
  });
});
