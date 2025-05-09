const { assert, expect } = require("chai");
const { getPaymentTokenFromAPI } = require("./6-payment_token");

describe("getPaymentTokenFromAPI", function () {
  it("should return a resolved promise with correct data when success is true", function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.be.an("object");
        expect(response).to.have.property(
          "data",
          "Successful response from the API"
        );
        done();
      })
      .catch(done);
  });
});
