import ws from 'k6/ws';
import { check, fail } from 'k6';

export let options = {
    vus: 1000,
    duration: '1m',
};

export default function () {
    const url = 'ws://0.0.0.0:8080/chats/ws/1/';
    const params = {
        headers: {
            // 'Sec-WebSocket-Protocol': 'your-protocol',
        },
    };

    ws.connect(url, params, function (socket) {
      let connected = false;

      socket.on('open', function open() {
        connected = true;
        socket.send('채팅입니다 ㅎㅇㅎㅇ');
      }); 

        socket.on('error', function (e) {
            if (e.error() != 'websocket: close sent') {
              fail(e.error());
            }
        });

        socket.setTimeout(function () {
          if (connected) {
            check(connected, (connected)=>connected === true);
          } else {
            fail('Connection was not established within the expected time');
          }
          socket.close();
        }, 1000);
    });
}
