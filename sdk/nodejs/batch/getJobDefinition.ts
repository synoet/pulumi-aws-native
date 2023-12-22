// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Batch::JobDefinition
 */
export function getJobDefinition(args: GetJobDefinitionArgs, opts?: pulumi.InvokeOptions): Promise<GetJobDefinitionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:batch:getJobDefinition", {
        "jobDefinitionArn": args.jobDefinitionArn,
    }, opts);
}

export interface GetJobDefinitionArgs {
    jobDefinitionArn: string;
}

export interface GetJobDefinitionResult {
    readonly containerOrchestrationType?: string;
    readonly jobDefinitionArn?: string;
    readonly revision?: number;
    readonly status?: string;
    /**
     * A key-value pair to associate with a resource.
     */
    readonly tags?: any;
}
/**
 * Resource Type definition for AWS::Batch::JobDefinition
 */
export function getJobDefinitionOutput(args: GetJobDefinitionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetJobDefinitionResult> {
    return pulumi.output(args).apply((a: any) => getJobDefinition(a, opts))
}

export interface GetJobDefinitionOutputArgs {
    jobDefinitionArn: pulumi.Input<string>;
}
