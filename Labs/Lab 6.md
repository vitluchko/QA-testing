- ### 1.
![image](https://github.com/vitluchko/QA-testing/assets/98816838/29712d95-4b13-442f-9585-5994a1341cb1)

- ### 2.
![image](https://github.com/vitluchko/QA-testing/assets/98816838/99bd3b2a-5920-4e1f-ac0f-c351753da7b1)

- ### Tests for GET Comments <i>(find all)</i>
```js
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Body contains string",() => {
  pm.expect(pm.response.text()).to.include("name");
});

pm.test("Response time is less than 200ms", () => {
  pm.expect(pm.response.responseTime).to.be.below(200);
});
```

- ### Test for GET Comment by ID <i>(find)</i>
```js
const jsonData = pm.response.json();
pm.test("Test data type of the response", () => {
  pm.expect(jsonData.name).to.be.a("string");
  pm.expect(jsonData.email).to.be.not.null;
});
```

- ### Tests for PUT Comment by ID <i>(update)</i>
```js
pm.test("Status code is 200", function () {
	pm.response.to.have.status(200);
});

const jsonData = pm.response.json();
pm.test("Test data type of the response", () => {
  pm.expect(jsonData.cars).to.be.not.null;
});
```
