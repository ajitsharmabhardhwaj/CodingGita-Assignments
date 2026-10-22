// Question-1
// for(let i=50; i>=1; i-=1){
//     if (i%3==0 && i%9!=0){
//         console.log(i)
//     }
// }

// Question-2
// let n="4729"
// let prod = 1
// for (let i=0; i<n.length-1; i+=1){
//     if (n[i]%2!=0){
//         prod*=n[i]

//     }
    
// }
// console.log(prod)

// Question-3
// let word ="Programming"
// for(let i=word.length-1; i>=0; i-=1){
//     if (word[i]!="a" && word[i]!="u" && word[i]!="o" && word[i]!="i" && word[i]!="e" ){
//        console.log(word[i]) 
//     }
    
// }

// Question-4
// let a=0
// let b=1
// let fib_series = "0 1 "
// for(let i=1; i<=13; i+=1){
//     c=a+b
//     fib_series+=c+" "
//     a=b
//     b=c
//     // console.log(fib_series)
// }

// rev=""
// for(let i=String(fib_series.length)-1; i>=0; i-=1){
//     rev+=fib_series[i]
    
// }
// console.log(rev)

// Question-5
// let num=121
// rev=0
// for(let i=1; i<=3; i+=1){
//     rev=rev*10+num%10
//     // console.log(rev)
//     num=Math.floor(num/10)

// }
// if(num=rev){
//     console.log("palindrome")
// }else{
//     console.log("not")
// }

// Question-6
// let arr = [12, 45, 7, 23, 56, 89, 34]
// for(let i=arr.length-1; i>=0; i-=1){
//     if (arr[i]>50){
//         console.log(arr[i])
//     }
// }

// Question-7
// let tem = [32, 28, 41, 19, 35, 27, 38]
// let count=0
// for(let i=tem.length-1; i>=0; i-=1){
//     if (tem[i]<30){
//         count+=1
//     }

// }
// console.log(count)

// Question-8
// let num=13
// let binery=0
// for(;num>0;){
//     let remaninder=num%2
//     binery=remaninder+binery
//     num=Math.floor(num/2)
// console.log(binery)
// }


// Question-9
// let score = [90, 85, 70, 95, 60, 88, 75]
// for(let i=score.length-1; i>=0; i-=1){
//     if (score[i]>80){
//         console.log(i,score[i])
//         break
//     }
// }

// Question-10
// for (let i=40; i>=1; i-=1){
//     if (i!=i*i){
//         continue
//         console.log(i)
        
//     }
// }



