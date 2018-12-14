# Chat_Robot

## Usage
### Initial State : ```user```

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
>>>    平手

> * go to user

---
## Finite State Machine
### Remove back flow
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


