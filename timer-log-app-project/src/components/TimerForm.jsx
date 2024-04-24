import { useState } from "react";

export default function TimerForm(props){

    const [forms, setForms]=useState({title:props.title, project: props.project})

    const submitText=props.title ? 'Update' : 'Create';
    return (
        <div className="flex justify-center">
            <div className="bg-white shadow-md rounded-lg w-1/3">
                <div className="p-4">
                    <form className="space-y-4">
                        <div className="flex flex-col">
                            <label htmlFor="title" className="text-sm font-semibold text-gray-600">Title</label>
                            <input 
                                id="title"
                                type="text"
                                value={forms.title}
                                onChange={props.handleTitleChange}
                                className="border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-400"
                            />
                        </div>
                        <div className="flex flex-col">
                            <label htmlFor="project" className="text-sm font-semibold text-gray-600">Project</label>
                            <input 
                                id="project"
                                type="text"
                                value={forms.project}
                                onChange={props.handleProjectChange}
                                className="border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-400"
                            />
                        </div>
                        <div className="flex justify-between">
                            <button className="bg-blue-500 text-white px-4 py-2 rounded-md">{submitText}</button>
                            <button className="bg-red-500 text-white px-4 py-2 rounded-md">Cancel</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );

}