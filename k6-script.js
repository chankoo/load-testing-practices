import http from 'k6/http';
import { sleep, check, fail } from 'k6';


export let options = {
  vus: 1000,
  duration: "5m"
};

export default function () {
  const url = 'http://0.0.0.0:8000/api/posts/';
  sleep(1);
  const res = http.get(url);
  const checkResult = check(res, {
    'is status 200': (r) => r.status === 200,
  });
  if (!checkResult) {
    fail('Failed due to an unexpected status code: ' + res.status);
  }
}
