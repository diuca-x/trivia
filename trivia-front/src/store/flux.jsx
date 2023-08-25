import { json } from "react-router-dom";

const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			
		},
		actions: {
			// Use getActions to call a function within a fuction
			//global_timer: (time) => {
				//const store = getStore()
				
				//setStore({...store, time : time})
			//}
			
			
		}
	};
};

export default getState;