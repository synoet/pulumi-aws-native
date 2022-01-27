// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::AppRunner::Service resource specifies an AppRunner Service.
 */
export class Service extends pulumi.CustomResource {
    /**
     * Get an existing Service resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Service {
        return new Service(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apprunner:Service';

    /**
     * Returns true if the given object is an instance of Service.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Service {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Service.__pulumiType;
    }

    /**
     * Autoscaling configuration ARN
     */
    public readonly autoScalingConfigurationArn!: pulumi.Output<string | undefined>;
    public readonly encryptionConfiguration!: pulumi.Output<outputs.apprunner.ServiceEncryptionConfiguration | undefined>;
    public readonly healthCheckConfiguration!: pulumi.Output<outputs.apprunner.ServiceHealthCheckConfiguration | undefined>;
    public readonly instanceConfiguration!: pulumi.Output<outputs.apprunner.ServiceInstanceConfiguration | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the AppRunner Service.
     */
    public /*out*/ readonly serviceArn!: pulumi.Output<string>;
    /**
     * The AppRunner Service Id
     */
    public /*out*/ readonly serviceId!: pulumi.Output<string>;
    /**
     * The AppRunner Service Name.
     */
    public readonly serviceName!: pulumi.Output<string | undefined>;
    /**
     * The Service Url of the AppRunner Service.
     */
    public /*out*/ readonly serviceUrl!: pulumi.Output<string>;
    public readonly sourceConfiguration!: pulumi.Output<outputs.apprunner.ServiceSourceConfiguration>;
    /**
     * AppRunner Service status.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.apprunner.ServiceTag[] | undefined>;

    /**
     * Create a Service resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServiceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.sourceConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourceConfiguration'");
            }
            resourceInputs["autoScalingConfigurationArn"] = args ? args.autoScalingConfigurationArn : undefined;
            resourceInputs["encryptionConfiguration"] = args ? args.encryptionConfiguration : undefined;
            resourceInputs["healthCheckConfiguration"] = args ? args.healthCheckConfiguration : undefined;
            resourceInputs["instanceConfiguration"] = args ? args.instanceConfiguration : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["sourceConfiguration"] = args ? args.sourceConfiguration : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["serviceArn"] = undefined /*out*/;
            resourceInputs["serviceId"] = undefined /*out*/;
            resourceInputs["serviceUrl"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["autoScalingConfigurationArn"] = undefined /*out*/;
            resourceInputs["encryptionConfiguration"] = undefined /*out*/;
            resourceInputs["healthCheckConfiguration"] = undefined /*out*/;
            resourceInputs["instanceConfiguration"] = undefined /*out*/;
            resourceInputs["serviceArn"] = undefined /*out*/;
            resourceInputs["serviceId"] = undefined /*out*/;
            resourceInputs["serviceName"] = undefined /*out*/;
            resourceInputs["serviceUrl"] = undefined /*out*/;
            resourceInputs["sourceConfiguration"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Service.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Service resource.
 */
export interface ServiceArgs {
    /**
     * Autoscaling configuration ARN
     */
    autoScalingConfigurationArn?: pulumi.Input<string>;
    encryptionConfiguration?: pulumi.Input<inputs.apprunner.ServiceEncryptionConfigurationArgs>;
    healthCheckConfiguration?: pulumi.Input<inputs.apprunner.ServiceHealthCheckConfigurationArgs>;
    instanceConfiguration?: pulumi.Input<inputs.apprunner.ServiceInstanceConfigurationArgs>;
    /**
     * The AppRunner Service Name.
     */
    serviceName?: pulumi.Input<string>;
    sourceConfiguration: pulumi.Input<inputs.apprunner.ServiceSourceConfigurationArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.apprunner.ServiceTagArgs>[]>;
}
