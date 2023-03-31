require("dotenv").config();
const { Configuration, OpenAIApi } = require("openai");

const config = new Configuration({
    apiKey: process.env.OPENAI_API_ENV,
    organization: process.env.OPENAI_ORG_ID,
});

const openai = new OpenAIApi(config);

const gerarDescricao = async (produto) => {
    const prompt = `Gerar uma descrição para o seguinte produto: ${produto}`;

    try {
        const completion = await openai.createCompletion({
            model: "text-davinci-003",
            prompt: prompt,
            max_tokens: 2046});
        return completion.data.choices[0].text;
    } catch (error) {
        if(error.response) {
            console.log(error.response.data);
            console.log(error.response.status);
        } else {
            console.log(error);
        }
    };

}

(async () => {
    const descricao = await gerarDescricao("Notebook Dell Inspiron 15 5000");
    console.log(descricao);
})();


    