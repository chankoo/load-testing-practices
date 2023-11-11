import http from 'k6/http';
import { sleep, check, fail } from 'k6';


export let options = {
  vus: 1000,
  duration: "5m"
};

export default function () {
  const url = 'http://0.0.0.0:8000/api/posts/';
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const res = http.get(url, params);
  const checkResult = check(res, {
    'is status 200': (r) => r.status === 200,
  });
  if (!checkResult) {
    fail('Failed due to an unexpected status code: ' + res.status);
  }
  sleep(1);
}
