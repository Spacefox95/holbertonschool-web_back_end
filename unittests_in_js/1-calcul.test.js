const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("Addition", function () {
  it("Sum when both are integers.", () => {
    assert.strictEqual(calculateNumber(1, 3, "SUM"), 4);
  });

  it("Sum when b is a float.", () => {
    assert.strictEqual(calculateNumber(1, 3.7, "SUM"), 5);
  });

  it("Sum when a is rounded down & b is rounded up.", () => {
    assert.strictEqual(calculateNumber(1.2, 3.7, "SUM"), 5);
  });

  it("Sum when a is a float.", () => {
    assert.strictEqual(calculateNumber(1.2, 3, "SUM"), 4);
  });

  describe("Substraction", function () {
		it("Subtract when both are integers.", () => {
			assert.strictEqual(calculateNumber(1, 3, "SUBTRACT"), -2);
	});

	it("Subtract when a is a float.", () => {
			assert.strictEqual(calculateNumber(1.2, 3, "SUBTRACT"), -2);
	});

	it("Subtract when b is a float.", () => {
			assert.strictEqual(calculateNumber( 1, 3.7, "SUBTRACT", ), -3);
	});
    it("Subtract when a is rounded up & b is rounded down.", () => {
      assert.strictEqual(calculateNumber(1.7, 3.2, "SUBTRACT"), -1);
    });

    it("Subtract when both are rounded up.", () => {
      assert.strictEqual(calculateNumber(1.5, 3.7, "SUBTRACT"), -2);
    });

    it("Sum when both are rounded up.", () => {
      assert.strictEqual(calculateNumber(1.4, 4.5, "SUBTRACT"), -4);
    });
		it("Subtract when both are rounded down.", () => {
			assert.strictEqual(calculateNumber(1.7, 3.7, "SUBTRACT"), -2);
	});
  });

  describe("Division", function () {
    it("Divide when both are rounded up.", () => {
      assert.strictEqual(calculateNumber(1.5, 3.7, "DIVIDE"), 0.5);
    });

    it("Sum when both are rounded up.", () => {
      assert.strictEqual(calculateNumber(1.4, 4.5, "DIVIDE"), 0.2);
    });

    it("Sum when both are rounded up.", () => {
      assert.strictEqual(calculateNumber(1.4, 0, "DIVIDE"), "Error");
    });

    it("Divide when a = 0", () => {
      assert.strictEqual(calculateNumber(0, 42, "DIVIDE"), 0);
    });
  });
});

describe("Error", function () {
  it("Type is not a string.", () => {
    assert.strictEqual(calculateNumber(2, 1, 3), "Error");
  });
});
