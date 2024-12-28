
function checkEligibility(person) {
    // Define required skills and eligibility criteria
    const requiredSkills = ['JavaScript', 'React', 'Node.js'];
    const minAge = 18;
    const minExperience = 2; // in years

    // Check eligibility using multiple conditions
    if (person.age >= minAge && person.experience >= minExperience && requiredSkills.every(skill => person.skills.includes(skill))) {
        console.log(`${person.name} is eligible for the task.`);
    } else {
        console.log(`${person.name} is not eligible for the task.`);
        // Check specific reasons for ineligibility
        if (person.age < minAge) {
            console.log("- Reason: Must be at least 18 years old.");
        }
        if (person.experience < minExperience) {
            console.log("- Reason: Must have at least 2 years of experience.");
        }
        const missingSkills = requiredSkills.filter(skill => !person.skills.includes(skill));
        if (missingSkills.length > 0) {
            console.log(`- Reason: Missing skills - ${missingSkills.join(', ')}`);
        }
    }
}

// Example person objects
const person1 = {
    name: 'Alice',
    age: 25,
    experience: 3,
    skills: ['JavaScript', 'React', 'Node.js','machine learning']
};

const person2 = {
    name: 'Bob',
    age: 17,
    experience: 3,
    skills: ['JavaScript', 'Node.js']
};

const person3 = {
    name: 'Charlie',
    age: 30,
    experience: 1,
    skills: ['JavaScript', 'React']
};


checkEligibility(person1); // Eligible
checkEligibility(person2); // Not eligible (age)
checkEligibility(person3); // Not eligible (experience)
