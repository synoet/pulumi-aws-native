// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The resource schema to create a CodeArtifact domain.
 */
export function getDomain(args: GetDomainArgs, opts?: pulumi.InvokeOptions): Promise<GetDomainResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:codeartifact:getDomain", {
        "arn": args.arn,
    }, opts);
}

export interface GetDomainArgs {
    /**
     * The ARN of the domain.
     */
    arn: string;
}

export interface GetDomainResult {
    /**
     * The ARN of the domain.
     */
    readonly arn?: string;
    /**
     * The name of the domain. This field is used for GetAtt
     */
    readonly name?: string;
    /**
     * The 12-digit account ID of the AWS account that owns the domain. This field is used for GetAtt
     */
    readonly owner?: string;
    /**
     * The access control resource policy on the provided domain.
     */
    readonly permissionsPolicyDocument?: any;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.codeartifact.DomainTag[];
}
/**
 * The resource schema to create a CodeArtifact domain.
 */
export function getDomainOutput(args: GetDomainOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDomainResult> {
    return pulumi.output(args).apply((a: any) => getDomain(a, opts))
}

export interface GetDomainOutputArgs {
    /**
     * The ARN of the domain.
     */
    arn: pulumi.Input<string>;
}
