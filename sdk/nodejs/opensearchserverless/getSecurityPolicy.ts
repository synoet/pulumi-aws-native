// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Amazon OpenSearchServerless security policy resource
 */
export function getSecurityPolicy(args: GetSecurityPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetSecurityPolicyResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:opensearchserverless:getSecurityPolicy", {
        "name": args.name,
        "type": args.type,
    }, opts);
}

export interface GetSecurityPolicyArgs {
    /**
     * The name of the policy
     */
    name: string;
    type: enums.opensearchserverless.SecurityPolicyType;
}

export interface GetSecurityPolicyResult {
    /**
     * The description of the policy
     */
    readonly description?: string;
    /**
     * The JSON policy document that is the content for the policy
     */
    readonly policy?: string;
}

export function getSecurityPolicyOutput(args: GetSecurityPolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSecurityPolicyResult> {
    return pulumi.output(args).apply(a => getSecurityPolicy(a, opts))
}

export interface GetSecurityPolicyOutputArgs {
    /**
     * The name of the policy
     */
    name: pulumi.Input<string>;
    type: pulumi.Input<enums.opensearchserverless.SecurityPolicyType>;
}
