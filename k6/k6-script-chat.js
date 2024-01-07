import ws from 'k6/ws';
import { check } from 'k6';

var vus = 100;

export let options = {
    vus: vus,
    duration: '3m', // max duration
    iterations: vus * 6,  // 10s * 6
};

export default function () {
    const url = 'ws://alb-sample-chat-1479566983.ap-northeast-2.elb.amazonaws.com/chats/ws/1/';
    const params = {};
    const msg = '채팅입니다 ㅎㅇㅎㅇ';
    const sendInterval = 1000;  // 1000ms 마다 메시지 전송
    const connectionSec = 10;  // 10s 동안 커넥션 유지

    const res = ws.connect(url, params, function (socket) {
      socket.on('open', function open() {
        socket.setInterval(function timeout() {
          socket.send(msg);
        }, sendInterval);
      });

      socket.setTimeout(function () {
        socket.close();
      }, 1000 * connectionSec);
    });

    check(res, { 'Connected successfully': (r) => r && r.status === 101 });
}
