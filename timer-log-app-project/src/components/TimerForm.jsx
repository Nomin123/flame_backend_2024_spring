import { useState } from "react";

export default function TimerForm({
    id,
    title: initialTitle = "",
    project: initialProject = "",
    onFormSubmit,
    onFormClose,
}) {
    const [title, setTitle] = useState(initialTitle);
    const [project, setProject] = useState(initialProject);

    const handleTitleChange = (e) => {
        setTitle(e.target.value);

    };

    const handleProjectChange = (e) => {
        setProject(e.target.value);

    };

    const handleSubmit = (e) => {
        onFormSubmit({
            id,
            title,
            project,

        });

    };



    const submitText = id ? 'Update' : 'Create';

    return (
        <div className="flex justify-center">
            <div className="bg-white shadow-md rounded-lg w-1/3">
                <div className="p-4">
                    <form className="space-y-4">
                        <div className="flex flex-col">
                            <label
                                htmlFor="title"
                                className="text-sm font-semibold text-gray-600"
                            >
                                Title
                            </label>
                            <input
                                id="title"
                                type="text"
                                value={title}
                                onChange={handleTitleChange}
                                className="border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-400"
                            />
                        </div>
                        <div className="flex flex-col">
                            <label
                                htmlFor="project"
                                className="text-sm font-semibold text-gray-600"
                            >
                                Project
                            </label>
                            <input
                                id="project"
                                type="text"
                                value={project}
                                onChange={handleProjectChange}
                                className="border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-400"
                            />
                        </div>
                        <div className="flex justify-between">
                            <button
                                className="bg-blue-500 text-white px-4 py-2 rounded-md"
                                onClick={handleSubmit}
                            >
                                {submitText}
                            </button>
                            <button
                                className="bg-red-500 text-white px-4 py-2 rounded-md"
                                onClick={onFormClose}
                            >
                                Cancel
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}