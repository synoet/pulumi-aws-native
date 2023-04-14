// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Greengrass::FunctionDefinitionVersion
 */
export function getFunctionDefinitionVersion(args: GetFunctionDefinitionVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetFunctionDefinitionVersionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:greengrass:getFunctionDefinitionVersion", {
        "id": args.id,
    }, opts);
}

export interface GetFunctionDefinitionVersionArgs {
    id: string;
}

export interface GetFunctionDefinitionVersionResult {
    readonly id?: string;
}
/**
 * Resource Type definition for AWS::Greengrass::FunctionDefinitionVersion
 */
export function getFunctionDefinitionVersionOutput(args: GetFunctionDefinitionVersionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFunctionDefinitionVersionResult> {
    return pulumi.output(args).apply((a: any) => getFunctionDefinitionVersion(a, opts))
}

export interface GetFunctionDefinitionVersionOutputArgs {
    id: pulumi.Input<string>;
}
