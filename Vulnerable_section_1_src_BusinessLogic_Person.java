 package BusinessLogic;
 
 import javax.servlet.http.HttpServlet;
 import java.util.Date;
 
 /**
 	private String email;
 	private String password; //needs encripting
 	private Date dob;
 	private double height;
 	private double weight;
 	private char gender;
 		this.email = email;
 		this.password = password;
 		this.dob = dob;
 		this.height = height;
 		this.weight = weight;
 		this.gender = gender;
     	//connect.pushUser(this);
 	}
 	
 	public void setMealplan(MealPlanner mealplan){
 		this.mealplan = mealplan;
 	}
 	public Date getDob(){
 		return dob;
 	}
 	public double getHeight(){
 		return height;
 	}
 	public MealPlanner getMealplan(){
 		return mealplan;
 	}
 
 	//use these setters if user changes age weight etc.
 	public void setName(String name){