# Chat_Robot
* A chat bot on FB messenger.
* It's a Tic-tac-toe game. 
* You are "o", the bot is "x".
* After send a text, it will return two image.
  > text: `A1`, `A2`, `A3`, `B1`, `B2`, `B3`, `C1`, `C2`, `C3`
* One is your choice, the other is the bot's choice.
* You can send `init` to clear at any time.
* Or send anything to see tutorial.

## Dependencies
* transitions
  * to implement FSM
* pillow
  * to make image
* pyimgur
  * to upload image to imgur.com
* protobuf
  * record states of users
  * to handle multiple users
* psycopg2
  * postgreSQL for python
  * to record url in imgur.com to avoid upload too many times
* pygraphviz
  * to draw FSM

## Deploy
* heroku
* docker

## FB Fan Page
* [圈圈叉叉](https://www.facebook.com/%E5%9C%88%E5%9C%88%E5%8F%89%E5%8F%89-276838406357095/?modal=admin_todo_tour)
* It's public.


## Usage
### Initial State : ```user```

### You can type `init` at any time to go back to ```user``` state

### Input a position to start the ~~game~~ bot
 ![](https://i.imgur.com/T0Qd8Va.png)

### Example : `user` -> `A1` -> `A1B1` -> `A1B1A3` -> `A1B1A3C2`

### user

> * Input: **A1**
>> * go to A1

### A1
>> * Reply: 
>>>  ![](https://i.imgur.com/vs8pO8r.png)  ![](https://i.imgur.com/xVUffK5.png)

> * Input: **B1**
>> * go to A1B1

### A1B1
>> *   Reply:
>>>   ![](https://i.imgur.com/q9VW3zQ.png)   ![](https://i.imgur.com/KnLPIbW.png)

> *  Input: **A3**
>> * go to A1B1A3

### A1B1A3
>> *  Reply:
>>>   ![](https://i.imgur.com/R2cNI2q.png)   ![](https://i.imgur.com/8Mkfjcy.png)

> *  Input: **C2**
>> *  go to A1B1A3C2

### A1B1A3C2
>> *  Reply:
>>>   ![](https://i.imgur.com/xtpS31q.png)   ![](https://i.imgur.com/Q6gWhqW.png)
>>>    End in a tie

> * go to user

---
## Finite State Machine
 > NOT complete FSM
 >> The complete image is too big to push to github( 176 MB )
 
 > So split to 9 images
 
 > Removed the back flow
 >> The fsm which has back flow(to user) will seem so mussy
   * A1
    ![A1](./fsm/A1_NoBack.png)
   * B1
    ![B1](./fsm/B1_NoBack.png)
   * C1
    ![C1](./fsm/C1_NoBack.png)
   * A2
    ![A2](./fsm/A2_NoBack.png)
   * B2
    ![B2](./fsm/B2_NoBack.png)
   * C2
    ![C2](./fsm/C2_NoBack.png)
   * A3
    ![A3](./fsm/A3_NoBack.png)
   * B3
    ![B3](./fsm/B3_NoBack.png)
   * C3
    ![C3](./fsm/C3_NoBack.png)


