// Question-1
// let i=10;
// do{
//     console.log(i)
//     i-=1
// }while(i>=1)

// Question-2
// let i=0;
// do{
//     console.log(i)
//     i+=2
// }while(i<=20)

//Question-3
// let sum=0
// let i=1;
// do{
//     sum+=i
//     i+=1
// }while(i<=5)
// console.log(sum)

// Question-4
// let prod=1
// let n=234
// do{
//     digit=n%10
//     prod*=digit
//     n=Math.floor(n/10)
// }while(n!=0)
// console.log(prod)

// Question-5
// let count=0
// let n=123456789
// do{
//     digit=n%10
//     count+=1
//     n=Math.floor(n/10)
// }while(n!=0)
// console.log(count)

// Question-6
// let base=5
// let exponent=2
// let i=1
// do{
//     digit=base**i
//     i+=1
// }while(i<=exponent)
// console.log(digit)

// Question-7
// let i=1;
// do{
//     if(i%4==0 && i%8!=0){
//         console.log(i)
//     }
//     i+=1
// }while(i<=100)

// Question-8
// let num=1221
// let orignal=num
// let rev=0
// do{
//     rev=rev*10+num%10
//     num=Math.floor(num/10)
// }while(num!=0)
// if (rev===orignal){
//     console.log("Palindrome")
// }else{
//     console.log("Not Palindrome")
// }

// Question-9
// let a=19
// let b=6
// let hcf=0
// let i=1
// let prod=1
// if(a>b){
//     hcf+=b
// }else{
//     hcf+=a
// }
// do{
//     if(a%i==0 && b%i==0){
//        prod*=i
//     }
//     i+=1
// }while(i<hcf)
// console.log(prod)

// Question-10
// let num=13
// let bag=""
// do{
//     digit=num%2
//     bag=digit+bag
//     num=Math.floor(num/2)
// }while(num!=0)
// console.log(bag)

