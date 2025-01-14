// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SageMaker::CodeRepository
 */
export function getCodeRepository(args: GetCodeRepositoryArgs, opts?: pulumi.InvokeOptions): Promise<GetCodeRepositoryResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:sagemaker:getCodeRepository", {
        "id": args.id,
    }, opts);
}

export interface GetCodeRepositoryArgs {
    id: string;
}

export interface GetCodeRepositoryResult {
    readonly gitConfig?: outputs.sagemaker.CodeRepositoryGitConfig;
    readonly id?: string;
    readonly tags?: outputs.sagemaker.CodeRepositoryTag[];
}
/**
 * Resource Type definition for AWS::SageMaker::CodeRepository
 */
export function getCodeRepositoryOutput(args: GetCodeRepositoryOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCodeRepositoryResult> {
    return pulumi.output(args).apply((a: any) => getCodeRepository(a, opts))
}

export interface GetCodeRepositoryOutputArgs {
    id: pulumi.Input<string>;
}
