// Description: This program takes user inputs and prints a short paragraph
//              describing the user based on their inputs
// Date:        July 21st - July 25th, 2024
// Author:      Jack Williams

// Input \\

const customerInfo = {
    firstName: 'Bartholomew',
    lastName: 'Turner',
    birthDate: '1958-9-23',
    gender: 'male',

    roomPref: ['early check-in', 'extra bed', 'extra key'],
    payMethod: 'credit card',

    mailAdd: {
        streetAdd: '102 Toby Rd',
        city: 'Gander',
        postCode: 'E4Q 5P0',
        province: 'NL',
    },

    emailAdd: 'bartturn0923@gmail.com',
    phoneNum: '+1 (709) 482-1029',

    checkDates: {
        checkIn: '2024-10-27',
        checkOut: '2024-10-30',
    },

    get birthYear() {
        return this.birthDate.substring(0, 4);
    },
    get checkOutYear() {
        return this.checkDates.checkOut.substring(0, 4);
    },
    get age() {
        return Number(this.checkOutYear) - Number(this.birthYear);
    },

    get checkInDay() {
        return this.checkDates.checkIn.substring(8, 10);
    },
    get checkOutDay() {
        return this.checkDates.checkOut.substring(8, 10);
    },
    get durStay() {
        return Number(this.checkOutDay) - Number(this.checkInDay);
    },

    // Output \\
    // I tried to make the paragraph fit on screen but it would mess up the formatting when displaying it \\

    get custDesc() {
        return `Our last customer was named ${this.firstName} ${this.lastName}. They are a ${this.age} year old ${this.gender}, who lives at ${this.mailAdd.streetAdd}, ${this.mailAdd.city}, ${this.mailAdd.postCode}, ${this.mailAdd.province}. They checked in on ${this.checkDates.checkIn}, where they stayed for ${this.durStay} days and checked out on ${this.checkDates.checkOut}. Their room preferences were ${this.roomPref[0]}, ${this.roomPref[1]}, and ${this.roomPref[2]}. They paid for their room via ${this.payMethod}. To get in contact with this customer, call them at ${this.phoneNum} or email them at ${this.emailAdd}.`;
    }
};

console.log(customerInfo.custDesc)

html = `<h3><p>${customerInfo.custDesc}</p></h3>`

document.body.innerHTML = html;