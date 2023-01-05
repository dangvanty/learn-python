// // num = int(input("Number of rows: "))

// // for i in range(num):
// //   for j in range(num - i - 1):
// //     print(end = " ")
// //   for j in range(i+1):
// //     print("*", end=" ")
// //   print()

// const test=(num)=>{
//   for (let i =0; i<num;i++){
//     let rows=''
//     for (let j = 0; j< num - i - 1 ; j++){
//       rows+=" "
//     }
//     for(let j=0;j< i+1;j++){
//       rows+="* "
//     }
//     console.log(rows)
//   }
// }
// test(5)

// const test=(a,b,c=8)=>{
//   const d=a+b+c
//   console.log(d)
// }
// test(1,1)
const a = [4,5,6,78,9,1,2]
const test = (a)=>{
  a.forEach(e => {
    if (e>6){
      
    }
    console.log(e)
  });
}
test(a)