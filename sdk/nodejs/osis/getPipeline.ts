// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.
 */
export function getPipeline(args: GetPipelineArgs, opts?: pulumi.InvokeOptions): Promise<GetPipelineResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:osis:getPipeline", {
        "pipelineArn": args.pipelineArn,
    }, opts);
}

export interface GetPipelineArgs {
    /**
     * The Amazon Resource Name (ARN) of the pipeline.
     */
    pipelineArn: string;
}

export interface GetPipelineResult {
    readonly bufferOptions?: outputs.osis.PipelineBufferOptions;
    readonly encryptionAtRestOptions?: outputs.osis.PipelineEncryptionAtRestOptions;
    /**
     * A list of endpoints that can be used for ingesting data into a pipeline
     */
    readonly ingestEndpointUrls?: string[];
    readonly logPublishingOptions?: outputs.osis.PipelineLogPublishingOptions;
    /**
     * The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
     */
    readonly maxUnits?: number;
    /**
     * The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
     */
    readonly minUnits?: number;
    /**
     * The Amazon Resource Name (ARN) of the pipeline.
     */
    readonly pipelineArn?: string;
    /**
     * The Data Prepper pipeline configuration in YAML format.
     */
    readonly pipelineConfigurationBody?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.osis.PipelineTag[];
    /**
     * The VPC interface endpoints that have access to the pipeline.
     */
    readonly vpcEndpoints?: outputs.osis.PipelineVpcEndpoint[];
}
/**
 * An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.
 */
export function getPipelineOutput(args: GetPipelineOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPipelineResult> {
    return pulumi.output(args).apply((a: any) => getPipeline(a, opts))
}

export interface GetPipelineOutputArgs {
    /**
     * The Amazon Resource Name (ARN) of the pipeline.
     */
    pipelineArn: pulumi.Input<string>;
}
