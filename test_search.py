from searchtweets import load_credentials, gen_rule_payload, collect_results

premium_search_args = load_credentials(filename="./creds.yml",
                                        yaml_key="test_app",
                                        env_overwrite=False)


# testing with a sandbox account, max 100 results
rule = gen_rule_payload("covidiots", results_per_call=100)

tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args)