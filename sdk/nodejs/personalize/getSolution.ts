// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Personalize::Solution.
 */
export function getSolution(args: GetSolutionArgs, opts?: pulumi.InvokeOptions): Promise<GetSolutionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:personalize:getSolution", {
        "solutionArn": args.solutionArn,
    }, opts);
}

export interface GetSolutionArgs {
    solutionArn: string;
}

export interface GetSolutionResult {
    readonly solutionArn?: string;
}
/**
 * Resource schema for AWS::Personalize::Solution.
 */
export function getSolutionOutput(args: GetSolutionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSolutionResult> {
    return pulumi.output(args).apply((a: any) => getSolution(a, opts))
}

export interface GetSolutionOutputArgs {
    solutionArn: pulumi.Input<string>;
}
