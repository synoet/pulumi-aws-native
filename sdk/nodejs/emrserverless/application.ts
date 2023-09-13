// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::EMRServerless::Application Type
 */
export class Application extends pulumi.CustomResource {
    /**
     * Get an existing Application resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Application {
        return new Application(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:emrserverless:Application';

    /**
     * Returns true if the given object is an instance of Application.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Application {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Application.__pulumiType;
    }

    /**
     * The ID of the EMR Serverless Application.
     */
    public /*out*/ readonly applicationId!: pulumi.Output<string>;
    public readonly architecture!: pulumi.Output<enums.emrserverless.ApplicationArchitecture | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the EMR Serverless Application.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Configuration for Auto Start of Application.
     */
    public readonly autoStartConfiguration!: pulumi.Output<outputs.emrserverless.ApplicationAutoStartConfiguration | undefined>;
    /**
     * Configuration for Auto Stop of Application.
     */
    public readonly autoStopConfiguration!: pulumi.Output<outputs.emrserverless.ApplicationAutoStopConfiguration | undefined>;
    public readonly imageConfiguration!: pulumi.Output<outputs.emrserverless.ApplicationImageConfigurationInput | undefined>;
    /**
     * Initial capacity initialized when an Application is started.
     */
    public readonly initialCapacity!: pulumi.Output<outputs.emrserverless.ApplicationInitialCapacityConfigKeyValuePair[] | undefined>;
    /**
     * Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
     */
    public readonly maximumCapacity!: pulumi.Output<outputs.emrserverless.ApplicationMaximumAllowedResources | undefined>;
    /**
     * User friendly Application name.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * Network Configuration for customer VPC connectivity.
     */
    public readonly networkConfiguration!: pulumi.Output<outputs.emrserverless.ApplicationNetworkConfiguration | undefined>;
    /**
     * EMR release label.
     */
    public readonly releaseLabel!: pulumi.Output<string>;
    /**
     * Tag map with key and value
     */
    public readonly tags!: pulumi.Output<outputs.emrserverless.ApplicationTag[] | undefined>;
    /**
     * The type of the application
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
     */
    public readonly workerTypeSpecifications!: pulumi.Output<outputs.emrserverless.ApplicationWorkerTypeSpecificationInputMap | undefined>;

    /**
     * Create a Application resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApplicationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.releaseLabel === undefined) && !opts.urn) {
                throw new Error("Missing required property 'releaseLabel'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["architecture"] = args ? args.architecture : undefined;
            resourceInputs["autoStartConfiguration"] = args ? args.autoStartConfiguration : undefined;
            resourceInputs["autoStopConfiguration"] = args ? args.autoStopConfiguration : undefined;
            resourceInputs["imageConfiguration"] = args ? args.imageConfiguration : undefined;
            resourceInputs["initialCapacity"] = args ? args.initialCapacity : undefined;
            resourceInputs["maximumCapacity"] = args ? args.maximumCapacity : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["networkConfiguration"] = args ? args.networkConfiguration : undefined;
            resourceInputs["releaseLabel"] = args ? args.releaseLabel : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["workerTypeSpecifications"] = args ? args.workerTypeSpecifications : undefined;
            resourceInputs["applicationId"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["applicationId"] = undefined /*out*/;
            resourceInputs["architecture"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["autoStartConfiguration"] = undefined /*out*/;
            resourceInputs["autoStopConfiguration"] = undefined /*out*/;
            resourceInputs["imageConfiguration"] = undefined /*out*/;
            resourceInputs["initialCapacity"] = undefined /*out*/;
            resourceInputs["maximumCapacity"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["networkConfiguration"] = undefined /*out*/;
            resourceInputs["releaseLabel"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["workerTypeSpecifications"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name", "type"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Application.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Application resource.
 */
export interface ApplicationArgs {
    architecture?: pulumi.Input<enums.emrserverless.ApplicationArchitecture>;
    /**
     * Configuration for Auto Start of Application.
     */
    autoStartConfiguration?: pulumi.Input<inputs.emrserverless.ApplicationAutoStartConfigurationArgs>;
    /**
     * Configuration for Auto Stop of Application.
     */
    autoStopConfiguration?: pulumi.Input<inputs.emrserverless.ApplicationAutoStopConfigurationArgs>;
    imageConfiguration?: pulumi.Input<inputs.emrserverless.ApplicationImageConfigurationInputArgs>;
    /**
     * Initial capacity initialized when an Application is started.
     */
    initialCapacity?: pulumi.Input<pulumi.Input<inputs.emrserverless.ApplicationInitialCapacityConfigKeyValuePairArgs>[]>;
    /**
     * Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
     */
    maximumCapacity?: pulumi.Input<inputs.emrserverless.ApplicationMaximumAllowedResourcesArgs>;
    /**
     * User friendly Application name.
     */
    name?: pulumi.Input<string>;
    /**
     * Network Configuration for customer VPC connectivity.
     */
    networkConfiguration?: pulumi.Input<inputs.emrserverless.ApplicationNetworkConfigurationArgs>;
    /**
     * EMR release label.
     */
    releaseLabel: pulumi.Input<string>;
    /**
     * Tag map with key and value
     */
    tags?: pulumi.Input<pulumi.Input<inputs.emrserverless.ApplicationTagArgs>[]>;
    /**
     * The type of the application
     */
    type: pulumi.Input<string>;
    /**
     * The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
     */
    workerTypeSpecifications?: pulumi.Input<inputs.emrserverless.ApplicationWorkerTypeSpecificationInputMapArgs>;
}
