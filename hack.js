


const wrapped = [{id: 3, title:"Let\'s have a look at the craziest day of your month!", content:"On the 2nd you spent 350.0$ on Public Transport"},{id: 1, title:"This month you have spent 420.0 USD", content:"This represents a 26.25% of your income"},{id: 2, title:"What did you mainly spend it on?", content:" "},{id: 1, title:"Your carbon footprint emissions amount was 0.7KgCO2e", content:"You\'re on the TOP 10 most sustainable users in your zone"},{id: 4, title:"What about your impulsive midnight purchases?", content:"You spent 350.0$ on Public Transport at 00:00"}];


const mood_wrapped = [{image: "./print__1.jpg"},
{image: "./print_2.jpg", img:""},
{image: "./print_3.jpg", img:"./pie___chart.png"},
{image: "./print_4.jpg", img:""},
{image: "./print__5.jpg", img:""}
];



/*
						{image: "https://i0.wp.com/texturefabrik.com/wp-content/uploads/2020/10/Texture-Fabrik-Kraft-Recycled-Paper-Textures-1_02.jpg?ssl=1"},
						{image: "https://i0.wp.com/texturefabrik.com/wp-content/uploads/2020/10/Texture-Fabrik-Kraft-Recycled-Paper-Textures-1_02.jpg?ssl=1"},
						{image: "https://i0.wp.com/texturefabrik.com/wp-content/uploads/2020/10/Texture-Fabrik-Kraft-Recycled-Paper-Textures-1_02.jpg?ssl=1"}
					]*/

var ID = 0;

function load(sum) {
	if (0<ID<wrapped.length) {
		ID = ID + sum;
		if (ID < 0 || ID >= wrapped.length) {
			// handle cases where ID goes beyond the bounds of wrapped array
			return;
		}
		const page = wrapped[ID];
		const mood = mood_wrapped[ID];
		
		// Get the element by its ID
		const myDiv = document.getElementById("myDiv");

		// Change the background image
		
		myDiv.style.backgroundImage = `url(${mood.image})`; 

		$('#title').html(`
						<tr>
						  <th scope="col" class="border-0 center-content font-large">
							<br>
							<br>
							<br>
							${page.title}
						  </th>
						</tr>
		`);
		if (ID==2) {
		$('#info').html(`
						 
						<tr class="h-25 ">
						  <td class="text-center border-0"><img src=${mood.img} style="width: 80%;"></td>
						</tr>
						
						<tr  style="height: 50px;">
						  <td colspan="3" class="center-content border-0 font-large" >
							<i class="fab fa-twitter m-3 "></i>
							<i class="fab fa-google m-3"></i>
							<i class="fab fa-instagram m-3"></i>
						  </td>
						</tr>
						 <tr>
							<td class="center-content border-0">Share it!</td>
						</tr>
						<br>	
		`);
			}
		else {
		$('#info').html(`
						
						  <tr>
							<td class="center-content border-0">${page.content}</td>
						</tr>
						
						<tr style="height: 50px;">
						  <td colspan="3" class="center-content border-0 font-large" >
							<i class="fab fa-twitter m-3 "></i>
							<i class="fab fa-google m-3"></i>
							<i class="fab fa-instagram m-3"></i>
						  </td>
						</tr>
						 <tr>
							<td class="center-content border-0">Share it!</td>
						</tr>
						<br>
						

			
		`);}
	};
};
$(document).ready(function() {
			load(0);
		});


