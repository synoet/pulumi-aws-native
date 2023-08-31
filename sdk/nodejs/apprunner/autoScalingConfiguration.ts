// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Describes an AWS App Runner automatic configuration resource that enables automatic scaling of instances used to process web requests. You can share an auto scaling configuration across multiple services.
 */
export class AutoScalingConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing AutoScalingConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AutoScalingConfiguration {
        return new AutoScalingConfiguration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apprunner:AutoScalingConfiguration';

    /**
     * Returns true if the given object is an instance of AutoScalingConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AutoScalingConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AutoScalingConfiguration.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of this auto scaling configuration.
     */
    public /*out*/ readonly autoScalingConfigurationArn!: pulumi.Output<string>;
    /**
     * The customer-provided auto scaling configuration name.  When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration. The auto scaling configuration name can be used in multiple revisions of a configuration.
     */
    public readonly autoScalingConfigurationName!: pulumi.Output<string | undefined>;
    /**
     * The revision of this auto scaling configuration. It's unique among all the active configurations ("Status": "ACTIVE") that share the same AutoScalingConfigurationName.
     */
    public /*out*/ readonly autoScalingConfigurationRevision!: pulumi.Output<number>;
    /**
     * It's set to true for the configuration with the highest Revision among all configurations that share the same AutoScalingConfigurationName. It's set to false otherwise. App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.
     */
    public /*out*/ readonly latest!: pulumi.Output<boolean>;
    /**
     * The maximum number of concurrent requests that an instance processes. If the number of concurrent requests exceeds this limit, App Runner scales the service up to use more instances to process the requests.
     */
    public readonly maxConcurrency!: pulumi.Output<number | undefined>;
    /**
     * The maximum number of instances that an App Runner service scales up to. At most MaxSize instances actively serve traffic for your service.
     */
    public readonly maxSize!: pulumi.Output<number | undefined>;
    /**
     * The minimum number of instances that App Runner provisions for a service. The service always has at least MinSize provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.
     */
    public readonly minSize!: pulumi.Output<number | undefined>;
    /**
     * A list of metadata items that you can associate with your auto scaling configuration resource. A tag is a key-value pair.
     */
    public readonly tags!: pulumi.Output<outputs.apprunner.AutoScalingConfigurationTag[] | undefined>;

    /**
     * Create a AutoScalingConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: AutoScalingConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["autoScalingConfigurationName"] = args ? args.autoScalingConfigurationName : undefined;
            resourceInputs["maxConcurrency"] = args ? args.maxConcurrency : undefined;
            resourceInputs["maxSize"] = args ? args.maxSize : undefined;
            resourceInputs["minSize"] = args ? args.minSize : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["autoScalingConfigurationArn"] = undefined /*out*/;
            resourceInputs["autoScalingConfigurationRevision"] = undefined /*out*/;
            resourceInputs["latest"] = undefined /*out*/;
        } else {
            resourceInputs["autoScalingConfigurationArn"] = undefined /*out*/;
            resourceInputs["autoScalingConfigurationName"] = undefined /*out*/;
            resourceInputs["autoScalingConfigurationRevision"] = undefined /*out*/;
            resourceInputs["latest"] = undefined /*out*/;
            resourceInputs["maxConcurrency"] = undefined /*out*/;
            resourceInputs["maxSize"] = undefined /*out*/;
            resourceInputs["minSize"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["autoScalingConfigurationName", "maxConcurrency", "maxSize", "minSize", "tags[*]"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AutoScalingConfiguration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AutoScalingConfiguration resource.
 */
export interface AutoScalingConfigurationArgs {
    /**
     * The customer-provided auto scaling configuration name.  When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration. The auto scaling configuration name can be used in multiple revisions of a configuration.
     */
    autoScalingConfigurationName?: pulumi.Input<string>;
    /**
     * The maximum number of concurrent requests that an instance processes. If the number of concurrent requests exceeds this limit, App Runner scales the service up to use more instances to process the requests.
     */
    maxConcurrency?: pulumi.Input<number>;
    /**
     * The maximum number of instances that an App Runner service scales up to. At most MaxSize instances actively serve traffic for your service.
     */
    maxSize?: pulumi.Input<number>;
    /**
     * The minimum number of instances that App Runner provisions for a service. The service always has at least MinSize provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.
     */
    minSize?: pulumi.Input<number>;
    /**
     * A list of metadata items that you can associate with your auto scaling configuration resource. A tag is a key-value pair.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.apprunner.AutoScalingConfigurationTagArgs>[]>;
}
