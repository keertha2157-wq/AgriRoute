# AgriRoute
An offline ,automated SMS/USSD routing
# AgriRoute: SMS-Based Rural Supply Chain Network

An offline, automated USSD and SMS routing platform that matches smallholder rural farmers with local truck drivers who have empty cargo space to prevent post-harvest crop spoilage.

## 🚀 Setup Steps & Environment Variables
1. *Clone the repository:*
   bash
   git clone https://github.com
   cd AgriRoute
   
2. *Install dependencies:*
   bash
   pip install flask twilio python-dotenv
   
3. *Configure Environment Variables (.env):*
   Create a .env file in the root directory and add the following keys:
   env
   PORT=5000
   TWILIO_ACCOUNT_SID=your_twilio_sid_here
   TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
   
4. *Run the application:*
   bash
   python app.py
