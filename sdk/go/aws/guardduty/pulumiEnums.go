// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package guardduty

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type DetectorCfnFeatureConfigurationName string

const (
	DetectorCfnFeatureConfigurationNameFlowLogs             = DetectorCfnFeatureConfigurationName("FLOW_LOGS")
	DetectorCfnFeatureConfigurationNameCloudTrail           = DetectorCfnFeatureConfigurationName("CLOUD_TRAIL")
	DetectorCfnFeatureConfigurationNameDnsLogs              = DetectorCfnFeatureConfigurationName("DNS_LOGS")
	DetectorCfnFeatureConfigurationNameS3DataEvents         = DetectorCfnFeatureConfigurationName("S3_DATA_EVENTS")
	DetectorCfnFeatureConfigurationNameEksAuditLogs         = DetectorCfnFeatureConfigurationName("EKS_AUDIT_LOGS")
	DetectorCfnFeatureConfigurationNameEbsMalwareProtection = DetectorCfnFeatureConfigurationName("EBS_MALWARE_PROTECTION")
	DetectorCfnFeatureConfigurationNameRdsLoginEvents       = DetectorCfnFeatureConfigurationName("RDS_LOGIN_EVENTS")
	DetectorCfnFeatureConfigurationNameLambdaNetworkLogs    = DetectorCfnFeatureConfigurationName("LAMBDA_NETWORK_LOGS")
	DetectorCfnFeatureConfigurationNameEksRuntimeMonitoring = DetectorCfnFeatureConfigurationName("EKS_RUNTIME_MONITORING")
)

func (DetectorCfnFeatureConfigurationName) ElementType() reflect.Type {
	return reflect.TypeOf((*DetectorCfnFeatureConfigurationName)(nil)).Elem()
}

func (e DetectorCfnFeatureConfigurationName) ToDetectorCfnFeatureConfigurationNameOutput() DetectorCfnFeatureConfigurationNameOutput {
	return pulumi.ToOutput(e).(DetectorCfnFeatureConfigurationNameOutput)
}

func (e DetectorCfnFeatureConfigurationName) ToDetectorCfnFeatureConfigurationNameOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationNameOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DetectorCfnFeatureConfigurationNameOutput)
}

func (e DetectorCfnFeatureConfigurationName) ToDetectorCfnFeatureConfigurationNamePtrOutput() DetectorCfnFeatureConfigurationNamePtrOutput {
	return e.ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(context.Background())
}

func (e DetectorCfnFeatureConfigurationName) ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationNamePtrOutput {
	return DetectorCfnFeatureConfigurationName(e).ToDetectorCfnFeatureConfigurationNameOutputWithContext(ctx).ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(ctx)
}

func (e DetectorCfnFeatureConfigurationName) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DetectorCfnFeatureConfigurationName) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DetectorCfnFeatureConfigurationName) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DetectorCfnFeatureConfigurationName) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DetectorCfnFeatureConfigurationNameOutput struct{ *pulumi.OutputState }

func (DetectorCfnFeatureConfigurationNameOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DetectorCfnFeatureConfigurationName)(nil)).Elem()
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToDetectorCfnFeatureConfigurationNameOutput() DetectorCfnFeatureConfigurationNameOutput {
	return o
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToDetectorCfnFeatureConfigurationNameOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationNameOutput {
	return o
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToDetectorCfnFeatureConfigurationNamePtrOutput() DetectorCfnFeatureConfigurationNamePtrOutput {
	return o.ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(context.Background())
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationNamePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DetectorCfnFeatureConfigurationName) *DetectorCfnFeatureConfigurationName {
		return &v
	}).(DetectorCfnFeatureConfigurationNamePtrOutput)
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToOutput(ctx context.Context) pulumix.Output[DetectorCfnFeatureConfigurationName] {
	return pulumix.Output[DetectorCfnFeatureConfigurationName]{
		OutputState: o.OutputState,
	}
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DetectorCfnFeatureConfigurationName) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DetectorCfnFeatureConfigurationNameOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DetectorCfnFeatureConfigurationName) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DetectorCfnFeatureConfigurationNamePtrOutput struct{ *pulumi.OutputState }

func (DetectorCfnFeatureConfigurationNamePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DetectorCfnFeatureConfigurationName)(nil)).Elem()
}

func (o DetectorCfnFeatureConfigurationNamePtrOutput) ToDetectorCfnFeatureConfigurationNamePtrOutput() DetectorCfnFeatureConfigurationNamePtrOutput {
	return o
}

func (o DetectorCfnFeatureConfigurationNamePtrOutput) ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationNamePtrOutput {
	return o
}

func (o DetectorCfnFeatureConfigurationNamePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*DetectorCfnFeatureConfigurationName] {
	return pulumix.Output[*DetectorCfnFeatureConfigurationName]{
		OutputState: o.OutputState,
	}
}

func (o DetectorCfnFeatureConfigurationNamePtrOutput) Elem() DetectorCfnFeatureConfigurationNameOutput {
	return o.ApplyT(func(v *DetectorCfnFeatureConfigurationName) DetectorCfnFeatureConfigurationName {
		if v != nil {
			return *v
		}
		var ret DetectorCfnFeatureConfigurationName
		return ret
	}).(DetectorCfnFeatureConfigurationNameOutput)
}

func (o DetectorCfnFeatureConfigurationNamePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DetectorCfnFeatureConfigurationNamePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DetectorCfnFeatureConfigurationName) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DetectorCfnFeatureConfigurationNameInput is an input type that accepts DetectorCfnFeatureConfigurationNameArgs and DetectorCfnFeatureConfigurationNameOutput values.
// You can construct a concrete instance of `DetectorCfnFeatureConfigurationNameInput` via:
//
//	DetectorCfnFeatureConfigurationNameArgs{...}
type DetectorCfnFeatureConfigurationNameInput interface {
	pulumi.Input

	ToDetectorCfnFeatureConfigurationNameOutput() DetectorCfnFeatureConfigurationNameOutput
	ToDetectorCfnFeatureConfigurationNameOutputWithContext(context.Context) DetectorCfnFeatureConfigurationNameOutput
}

var detectorCfnFeatureConfigurationNamePtrType = reflect.TypeOf((**DetectorCfnFeatureConfigurationName)(nil)).Elem()

type DetectorCfnFeatureConfigurationNamePtrInput interface {
	pulumi.Input

	ToDetectorCfnFeatureConfigurationNamePtrOutput() DetectorCfnFeatureConfigurationNamePtrOutput
	ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(context.Context) DetectorCfnFeatureConfigurationNamePtrOutput
}

type detectorCfnFeatureConfigurationNamePtr string

func DetectorCfnFeatureConfigurationNamePtr(v string) DetectorCfnFeatureConfigurationNamePtrInput {
	return (*detectorCfnFeatureConfigurationNamePtr)(&v)
}

func (*detectorCfnFeatureConfigurationNamePtr) ElementType() reflect.Type {
	return detectorCfnFeatureConfigurationNamePtrType
}

func (in *detectorCfnFeatureConfigurationNamePtr) ToDetectorCfnFeatureConfigurationNamePtrOutput() DetectorCfnFeatureConfigurationNamePtrOutput {
	return pulumi.ToOutput(in).(DetectorCfnFeatureConfigurationNamePtrOutput)
}

func (in *detectorCfnFeatureConfigurationNamePtr) ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationNamePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DetectorCfnFeatureConfigurationNamePtrOutput)
}

func (in *detectorCfnFeatureConfigurationNamePtr) ToOutput(ctx context.Context) pulumix.Output[*DetectorCfnFeatureConfigurationName] {
	return pulumix.Output[*DetectorCfnFeatureConfigurationName]{
		OutputState: in.ToDetectorCfnFeatureConfigurationNamePtrOutputWithContext(ctx).OutputState,
	}
}

type DetectorCfnFeatureConfigurationStatus string

const (
	DetectorCfnFeatureConfigurationStatusEnabled  = DetectorCfnFeatureConfigurationStatus("ENABLED")
	DetectorCfnFeatureConfigurationStatusDisabled = DetectorCfnFeatureConfigurationStatus("DISABLED")
)

func (DetectorCfnFeatureConfigurationStatus) ElementType() reflect.Type {
	return reflect.TypeOf((*DetectorCfnFeatureConfigurationStatus)(nil)).Elem()
}

func (e DetectorCfnFeatureConfigurationStatus) ToDetectorCfnFeatureConfigurationStatusOutput() DetectorCfnFeatureConfigurationStatusOutput {
	return pulumi.ToOutput(e).(DetectorCfnFeatureConfigurationStatusOutput)
}

func (e DetectorCfnFeatureConfigurationStatus) ToDetectorCfnFeatureConfigurationStatusOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationStatusOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DetectorCfnFeatureConfigurationStatusOutput)
}

func (e DetectorCfnFeatureConfigurationStatus) ToDetectorCfnFeatureConfigurationStatusPtrOutput() DetectorCfnFeatureConfigurationStatusPtrOutput {
	return e.ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(context.Background())
}

func (e DetectorCfnFeatureConfigurationStatus) ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationStatusPtrOutput {
	return DetectorCfnFeatureConfigurationStatus(e).ToDetectorCfnFeatureConfigurationStatusOutputWithContext(ctx).ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(ctx)
}

func (e DetectorCfnFeatureConfigurationStatus) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DetectorCfnFeatureConfigurationStatus) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DetectorCfnFeatureConfigurationStatus) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DetectorCfnFeatureConfigurationStatus) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DetectorCfnFeatureConfigurationStatusOutput struct{ *pulumi.OutputState }

func (DetectorCfnFeatureConfigurationStatusOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DetectorCfnFeatureConfigurationStatus)(nil)).Elem()
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToDetectorCfnFeatureConfigurationStatusOutput() DetectorCfnFeatureConfigurationStatusOutput {
	return o
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToDetectorCfnFeatureConfigurationStatusOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationStatusOutput {
	return o
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToDetectorCfnFeatureConfigurationStatusPtrOutput() DetectorCfnFeatureConfigurationStatusPtrOutput {
	return o.ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(context.Background())
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationStatusPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DetectorCfnFeatureConfigurationStatus) *DetectorCfnFeatureConfigurationStatus {
		return &v
	}).(DetectorCfnFeatureConfigurationStatusPtrOutput)
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToOutput(ctx context.Context) pulumix.Output[DetectorCfnFeatureConfigurationStatus] {
	return pulumix.Output[DetectorCfnFeatureConfigurationStatus]{
		OutputState: o.OutputState,
	}
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DetectorCfnFeatureConfigurationStatus) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DetectorCfnFeatureConfigurationStatusOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DetectorCfnFeatureConfigurationStatus) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DetectorCfnFeatureConfigurationStatusPtrOutput struct{ *pulumi.OutputState }

func (DetectorCfnFeatureConfigurationStatusPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DetectorCfnFeatureConfigurationStatus)(nil)).Elem()
}

func (o DetectorCfnFeatureConfigurationStatusPtrOutput) ToDetectorCfnFeatureConfigurationStatusPtrOutput() DetectorCfnFeatureConfigurationStatusPtrOutput {
	return o
}

func (o DetectorCfnFeatureConfigurationStatusPtrOutput) ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationStatusPtrOutput {
	return o
}

func (o DetectorCfnFeatureConfigurationStatusPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*DetectorCfnFeatureConfigurationStatus] {
	return pulumix.Output[*DetectorCfnFeatureConfigurationStatus]{
		OutputState: o.OutputState,
	}
}

func (o DetectorCfnFeatureConfigurationStatusPtrOutput) Elem() DetectorCfnFeatureConfigurationStatusOutput {
	return o.ApplyT(func(v *DetectorCfnFeatureConfigurationStatus) DetectorCfnFeatureConfigurationStatus {
		if v != nil {
			return *v
		}
		var ret DetectorCfnFeatureConfigurationStatus
		return ret
	}).(DetectorCfnFeatureConfigurationStatusOutput)
}

func (o DetectorCfnFeatureConfigurationStatusPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DetectorCfnFeatureConfigurationStatusPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DetectorCfnFeatureConfigurationStatus) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DetectorCfnFeatureConfigurationStatusInput is an input type that accepts DetectorCfnFeatureConfigurationStatusArgs and DetectorCfnFeatureConfigurationStatusOutput values.
// You can construct a concrete instance of `DetectorCfnFeatureConfigurationStatusInput` via:
//
//	DetectorCfnFeatureConfigurationStatusArgs{...}
type DetectorCfnFeatureConfigurationStatusInput interface {
	pulumi.Input

	ToDetectorCfnFeatureConfigurationStatusOutput() DetectorCfnFeatureConfigurationStatusOutput
	ToDetectorCfnFeatureConfigurationStatusOutputWithContext(context.Context) DetectorCfnFeatureConfigurationStatusOutput
}

var detectorCfnFeatureConfigurationStatusPtrType = reflect.TypeOf((**DetectorCfnFeatureConfigurationStatus)(nil)).Elem()

type DetectorCfnFeatureConfigurationStatusPtrInput interface {
	pulumi.Input

	ToDetectorCfnFeatureConfigurationStatusPtrOutput() DetectorCfnFeatureConfigurationStatusPtrOutput
	ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(context.Context) DetectorCfnFeatureConfigurationStatusPtrOutput
}

type detectorCfnFeatureConfigurationStatusPtr string

func DetectorCfnFeatureConfigurationStatusPtr(v string) DetectorCfnFeatureConfigurationStatusPtrInput {
	return (*detectorCfnFeatureConfigurationStatusPtr)(&v)
}

func (*detectorCfnFeatureConfigurationStatusPtr) ElementType() reflect.Type {
	return detectorCfnFeatureConfigurationStatusPtrType
}

func (in *detectorCfnFeatureConfigurationStatusPtr) ToDetectorCfnFeatureConfigurationStatusPtrOutput() DetectorCfnFeatureConfigurationStatusPtrOutput {
	return pulumi.ToOutput(in).(DetectorCfnFeatureConfigurationStatusPtrOutput)
}

func (in *detectorCfnFeatureConfigurationStatusPtr) ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(ctx context.Context) DetectorCfnFeatureConfigurationStatusPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DetectorCfnFeatureConfigurationStatusPtrOutput)
}

func (in *detectorCfnFeatureConfigurationStatusPtr) ToOutput(ctx context.Context) pulumix.Output[*DetectorCfnFeatureConfigurationStatus] {
	return pulumix.Output[*DetectorCfnFeatureConfigurationStatus]{
		OutputState: in.ToDetectorCfnFeatureConfigurationStatusPtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DetectorCfnFeatureConfigurationNameInput)(nil)).Elem(), DetectorCfnFeatureConfigurationName("FLOW_LOGS"))
	pulumi.RegisterInputType(reflect.TypeOf((*DetectorCfnFeatureConfigurationNamePtrInput)(nil)).Elem(), DetectorCfnFeatureConfigurationName("FLOW_LOGS"))
	pulumi.RegisterInputType(reflect.TypeOf((*DetectorCfnFeatureConfigurationStatusInput)(nil)).Elem(), DetectorCfnFeatureConfigurationStatus("ENABLED"))
	pulumi.RegisterInputType(reflect.TypeOf((*DetectorCfnFeatureConfigurationStatusPtrInput)(nil)).Elem(), DetectorCfnFeatureConfigurationStatus("ENABLED"))
	pulumi.RegisterOutputType(DetectorCfnFeatureConfigurationNameOutput{})
	pulumi.RegisterOutputType(DetectorCfnFeatureConfigurationNamePtrOutput{})
	pulumi.RegisterOutputType(DetectorCfnFeatureConfigurationStatusOutput{})
	pulumi.RegisterOutputType(DetectorCfnFeatureConfigurationStatusPtrOutput{})
}
