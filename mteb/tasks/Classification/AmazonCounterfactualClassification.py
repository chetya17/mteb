from ...abstasks import AbsTaskClassification, MultilingualTask

_LANGUAGES = ["en", "de", "en-ext", "ja"]


class AmazonCounterfactualClassification(MultilingualTask, AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "AmazonCounterfactualClassification",
            "hf_hub_name": "mteb/amazon_counterfactual",
            "description": "A collection of Amazon customer reviews annotated for counterfactual detection binary classification.",
            "reference": "https://arxiv.org/abs/2104.06893",
            "category": "s2s",
            "type": "Classification",
            "available_splits": ["train", "validation", "test"],
            "eval_langs": _LANGUAGES,
            "main_score": "accuracy",
            "n_splits": 10,
            "samples_per_label": 32,
        }